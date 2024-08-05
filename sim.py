import world
import ai
import display
import time

DIRECTIONS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

FACINGS = ['N', 'E', 'S', 'W']
VALID_COMMANDS = [
    'F', # Move forward
    'R', # Turn right
    'L', # Turn left
    'X', # Self-destruct
    'U' # Teleport/Open Door/Touch Goal
]

def run_sim(
    the_world, 
    max_turns=None, 
    log=None, 
    use_display=False,
    display_speed=0.5
):

    the_ai = ai.AI()

    agent_x, agent_y = the_world.get_startxy()
    agent_facing = the_world.get_start_face_dir()
    cells_visited = []
    turn = 1
    agent_cmd = "X"
    percepts = {}

    disp = None

    if use_display:
        import display
        disp = display.Display(
            the_world,
            agent_x,
            agent_y
        )

    if use_display:
        disp.update(
            agent_x, agent_y, agent_facing
        )
        time.sleep(display_speed)

    

    run = True
    while run:

        # What does the agent see?
        percepts = get_percepts(the_world, agent_x, agent_y, agent_facing)

        # Get agent's command
        agent_cmd = the_ai.update(percepts)

        # LOG ###############################################################
        write_to_log(
            log,
            f"Turn: {turn}"
        )
        write_to_log(
            log,
            f"   Start:    {agent_x},{agent_y}   Facing: {agent_facing}"
        )
        percept_str = ""
        i = 0
        for k,v in percepts.items():
            percept_str += f"{k} "
            for p in v:
                percept_str += f"{p} "
            if i < len(percepts)-1:
                percept_str += "\n             "
            i+=1
        write_to_log(
            log,
            f"   Percepts: {percept_str}"
        )
        write_to_log(
            log,
            f"   Command:  {agent_cmd}"
        )
        # ####################################################################

        # Move the agent
        if validate_agent_cmd(agent_cmd):

            new_agent_x = agent_x
            new_agent_y = agent_y

            match agent_cmd:
                case 'F':
                    dx, dy = DIRECTIONS[agent_facing]
                    new_agent_x = agent_x + dx
                    new_agent_y = agent_y + dy
                    if the_world.is_cell_enterable(new_agent_x, new_agent_y):
                        agent_x = new_agent_x
                        agent_y = new_agent_y
                case 'R':
                    agent_facing = turn_right(agent_facing)
                case 'L':
                    agent_facing = turn_left(agent_facing)
                case 'X':
                    write_to_log(
                        log,
                        f"FAILURE: Your agent triggered its self-destruct."
                    )
                    run = False
                    continue

            # if (new_agent_x != agent_x or new_agent_y != agent_y) and \
            #     the_world.is_cell_enterable(new_agent_x, new_agent_y):
                
            trigger = the_world.check_triggers(agent_x, agent_y, agent_cmd)
            match trigger[0]:
                case "DIE":
                    write_to_log(
                        log,
                        f"   Trigger:  Agent has been destroyed. FAILURE"
                    )
                    run = False
                case "TELEPORT":
                    write_to_log(
                        log,
                        f"   Trigger:  Teleported from {the_world.get_cell(agent_x, agent_y)} to {the_world.get_cell(trigger[1], trigger[2])}"
                    )
                    agent_x = trigger[1]
                    agent_y = trigger[2]
                    
                case "DOORS_OPEN":
                    write_to_log(
                        log,
                        f"   Trigger:  Doors opened."
                    )
                case "GOAL_TRIGGERED":
                    if trigger[1] == 0:
                        write_to_log(
                            log,
                            f"   Trigger:  Goal {trigger[2]}"
                        )
                        write_to_log(
                            log,
                            f"   Trigger:  You have completed this map in {turn} turns. SUCCESS"
                        )
                        run = False
                    else:
                        write_to_log(
                            log,
                            f"   Trigger:  Goal {trigger[2]}"
                        )
                case "NONE":
                    pass


            write_to_log(
                log,
                f"   End:      {agent_x},{agent_y}   Facing: {agent_facing}"
            )

            if max_turns is not None:
                if turn >= max_turns:
                    write_to_log(
                        log,
                        f"---MAX TURNS REACHED---"
                    )
                    run = False

        else:
            write_to_log(log, f"Invalid command: {agent_cmd}")
            run = False

        if use_display:
            disp.update(
                agent_x, agent_y, agent_facing
            )
            time.sleep(display_speed)

        turn += 1

    if use_display:
        disp.quit()

def get_percepts(the_world, agent_x, agent_y, agent_facing):
    percepts = {}
    percepts["X"] = [the_world.get_cell(agent_x, agent_y)]
    dx, dy = DIRECTIONS[agent_facing]
    ray = the_world.raycast(
        agent_x,
        agent_y,
        dx, dy
    )
    ray = the_world.prune_raycast(ray)
    percepts["F"] = ray
    return percepts


def validate_agent_cmd(cmd):
    return cmd in VALID_COMMANDS

def write_to_log(log, msg):
    if log is not None:
        log.write(f"{msg}\n")
        log.flush()
    else:
        print(msg)

def turn_right(cur_facing):
    match cur_facing:
        case 'N': return 'E'
        case 'E': return 'S'
        case 'S': return 'W'
        case 'W': return 'N'

def turn_left(cur_facing):
    match cur_facing:
        case 'N': return 'W'
        case 'W': return 'S'
        case 'S': return 'E'
        case 'E': return 'N'
