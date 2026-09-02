def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) == 0:
        return "R"

    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    # Use the opponent's most common move after enough games
    if len(opponent_history) < 10:
        return counter[opponent_history[-1]]

    # Look for patterns of different lengths
    for pattern_length in [5, 4, 3, 2, 1]:
        if len(opponent_history) <= pattern_length:
            continue

        pattern = opponent_history[-pattern_length:]

        matches = []

        for i in range(len(opponent_history) - pattern_length):
            if opponent_history[i:i + pattern_length] == pattern:
                matches.append(opponent_history[i + pattern_length])

        if matches:
            prediction = max(set(matches), key=matches.count)
            return counter[prediction]

    # Fallback: counter the opponent's last move
    return counter[opponent_history[-1]]