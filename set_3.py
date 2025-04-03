# no 1
def relationship_status(from_member, to_member, social_graph):
  if (to_member in social_graph[from_member]["following"]) and (from_member in social_graph[to_member]["following"]):
    return "friends"
  elif to_member in social_graph[from_member]["following"]:
    return "follower"
  elif from_member in social_graph[to_member]["following"]:
    return "followed by"
  else:
    return "no relationship"


# no 2
def tic_tac_toe(board):
  for row in board:
      row_symbols = set(row)
      if len(row_symbols) == 1 and row[0] != "":
          return row[0]

  for col in range(len(board)):
      column = []
      for row in range(len(board)):
          column.append(board[row][col])

      symbol = set(column)
      if len(symbol) == 1 and column[0] != "":
          return column[0]

  diag1 = []
  for i in range(len(board)):
      diag1.append(board[i][i])

  symbol = set(diag1)
  if len(symbol) == 1 and diag1[0] != "":
      return diag1[0]

  diag2 = []
  for i in range(len(board)):
      diag2.append(board[i][len(board) - 1 - i])

  symbol = set(diag2)
  if len(symbol) == 1 and diag2[0] != "":
      return diag2[0]

  return "NO WINNER"


# no 3
def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
        for leg in route_map:
            start, end = leg
            if start == current_stop:
                total_time += route_map[leg]["travel_time_mins"]
                current_stop = end
                break

    return total_time
