def printBoard(board):
  print("Current State of Board: \n");
  for i in range(9):
    if((i>0) and (i%3 == 0)):
      print("\n");
    if(board[i]==0):
      print("_ ",end=" ");
    elif(board[i]==-1):
      print("X ",end=" ");
    else:
      print("O ",end=" ");
  print("\n\n");

def user1Turn(board):
  while True:
    pos = int(input("Enter X's pos [1-9]: "));
    if board[pos-1] != 0:
      print("Wrong Move! Please Play again\n");
    else:
      board[pos-1] = -1;
      break;

def user2Turn(board):
  while True:
    pos = int(input("Enter O's pos [1-9]: "));
    if board[pos-1] != 0:
      print("Wrong Move! Please Play again\n");
    else:
      board[pos-1] = 1;
      break;

def minmax(board, player):
  x = analyseBoard(board);
  if(x!=0):
    return (x*player);
  pos=-1;
  value=-2;
  for i in range (9):
    if(board[i]==0):
      board[i]=player;
      score=-minmax(board,player*-1);
      board[i]=0;
      if(score>value):
        value=score;
        pos=i;
      if(value==1):
        break
  if(pos==-1):
    return 0;
  return value;

def compTurn(board):
  pos=-1;
  value=-2;
  for i in range (9):
    if(board[i]==0):
      board[i]=1;
      score=-minmax(board,-1);
      board[i]=0;
      if(score>value):
        value=score;
        pos=i;
      if(value==1):
        break
  board[pos]=1;

def analyseBoard(board):
  winPosb = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]];
  for i in range(8):
    if(board[winPosb[i][0]] != 0 and board[winPosb[i][0]]==board[winPosb[i][1]] and board[winPosb[i][1]]==board[winPosb[i][2]]):
      return board[winPosb[i][0]];
  return 0;


def main():
  choice = input("Press 1 for Single-Player or any other key for Multi-player: ");
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  if(choice=="1"):
    print("Computer: O Vs You: x\n")
    player = int(input("Enter 1 to play first and 2 to play second: "));
    for i in range(0,9):
      if(analyseBoard(board)!=0):
        break;
      if((i+player)%2==0):
        compTurn(board);
      else:
        printBoard(board);
        user1Turn(board);
  else:
    for i in range(9):
      if(analyseBoard(board)!=0):
        break;
      if(i%2==0):
        printBoard(board);
        user1Turn(board);
      else:
        printBoard(board);
        user2Turn(board);

  printBoard(board);
  if(analyseBoard(board)==0):
    print("Game Draw!");
  elif(analyseBoard(board)==-1):
    print("Player 1 wins!");
  else:
    print("Player 2 wins!");

main();               
