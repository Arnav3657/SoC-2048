# SoC-2048
Add epsilon-greedy exploration in agent.best_action():

Modify best_action to choose a random action with probability epsilon, otherwise choose the best action.

Allow epsilon to decay over episodes or be passed as a parameter.

Complete the play() function:

Implement proper game-over detection inside the IllegalAction exception handler.

Ensure the agent continues playing until no moves are possible.

Improve the training loop:

Spawn initial tiles in the board before starting.

Add periodic evaluation or logging to monitor learning progress.

Optional:
Improve the move logic (like _move_left)

Implementing the is_game_over() method to correctly detect terminal states
