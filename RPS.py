# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[], player_history=[]):
    # Ensure history and play_order are initialized correctly
    if 'play_order' not in player.__dict__:
        player.play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }
    # Append the opponent's last move to history
    if prev_play != "":
        opponent_history.append(prev_play)
    
    # Start with a fixed strategy for identification
    if len(opponent_history) <= 10:
        player_history.append("R")
        print(f"Round {len(opponent_history)}: Playing 'R' for identification.")
        return "R"  # Play "R" for the first 10 rounds to gather data
    
    # Countering Quincy (fixed pattern R, R, P, P, S)
    quincy_pattern = ["R", "P", "P", "S", "R"]
    
    # Determine if we are playing against Quincy by checking the pattern
    quincy_pattern_detected = all(
        opponent_history[i] == quincy_pattern[i % len(quincy_pattern)]
        for i in range(10)
    )
    
    if quincy_pattern_detected:
        print("Quincy")
        move_index = (len(opponent_history) - 1) % len(quincy_pattern)
        quincy_next_move = quincy_pattern[move_index]
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        counter_move = ideal_response[quincy_next_move]
        #print(f"Round {len(opponent_history)}: Detected Quincy. "
              #f"Quincy's next move is {quincy_next_move}. Playing counter move '{counter_move}'.")
        return counter_move
    
    mrugesh_pattern = ["R", "R", "P", "P", "P","P", "P", "P", "P", "P"]
    
    # Determine if we are playing against Quincy by checking the pattern
    mrugesh_pattern_detected = all(
        opponent_history[i] == mrugesh_pattern[i % len(mrugesh_pattern)]
        for i in range(10)
    )    
    if mrugesh_pattern_detected:
        print("Mrugesh")
            # Predict Mrugesh's next move based on his strategy
        most_frequent = max(set(opponent_history[-5:]), key=opponent_history[-5:].count)
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        counter_move = ideal_response[most_frequent]
        print(f"Round {len(opponent_history)}: Detected Mrugesh. "
                f"Most frequent move is '{most_frequent}'. Playing counter move '{counter_move}'.")
        return counter_move

    kris_pattern = ["P"] * 10
    
    kris_pattern_detected = opponent_history[-10:] == kris_pattern
    
    if kris_pattern_detected:
        print(f"Round {len(opponent_history)}: Detected Kris's pattern 'P P P P P P P P P P'. "
              "Switching to counter-Kris strategy.")    
    # If Kris is detected, always play the move that counters Kris's expected move
    if len(player_history) >= 1:
        last_player_move = player_history[-1]
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        kris_next_move = ideal_response[last_player_move]
        counter_move = ideal_response[kris_next_move]
        player_history.append(counter_move)
        return counter_move 
    
    # Update play_order based on opponent's last two moves
    if len(opponent_history) > 1:
        last_two = "".join(opponent_history[-2:])
        if len(last_two) == 2:
            player.play_order[last_two] += 1
            print(f"Updated play order for {last_two}: {player.play_order[last_two]}")
    
    # Predict Abbey's next move based on the most frequent pair
    if len(opponent_history) > 1:
        last_move = opponent_history[-1]
        potential_plays = {
            "R": {key: value for key, value in player.play_order.items() if key[0] == last_move},
            "P": {key: value for key, value in player.play_order.items() if key[0] == last_move},
            "S": {key: value for key, value in player.play_order.items() if key[0] == last_move}
        }

        # Find the most likely next move by considering context and frequency
        prediction = max(potential_plays[last_move], key=potential_plays[last_move].get)[1]

        # Abbey would predict your next move based on this and play to counter it
        # We'll counter Abbey's prediction
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        counter_move = ideal_response[prediction]
        
        print(f"Last move: {last_move}")
        print(f"Potential plays and their frequencies: {player.play_order}")
        print(f"Predicted next move by Abbey: {prediction}")
        print(f"Countering with: {counter_move}")
        
        player_history.append(counter_move)
        return counter_move
    


    # Fallback to a default move if no pattern is detected (or if in doubt)
    return "R"
