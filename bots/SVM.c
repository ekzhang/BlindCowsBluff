#include <stdio.h>

#include "bcb-client.h"

const char* BOT_NAME = "Not SVMBot";
int total_bet[100005], g_round;
int client_setup(int *argc, char ***argv)
{
	return 1;
}

void game_setup(const struct player_data* players, unsigned int numplayers)
{
	
}

void round_start(unsigned int rnum, unsigned int pstart, unsigned int ante)
{
	g_round = rnum;
}

int player_turn(const struct player_data* players, unsigned int numplayers)
{
  double average_player_card = 0.0;
  int i, num_active = 0, pending = 0;
  double factor1 = 0.0;
  for(i=0; i<numplayers; i++) {
    if(players[i].active && players[i].id != SELF.id) {
      factor1 = (double) (players[i].wager - total_bet[players[i].id] / g_round) / (total_bet[players[i].id] / g_round);
      total_bet[players[i].id] += players[i].wager;
      if (players[i].card > average_player_card)
        average_player_card = players[i].card;
      num_active++;
      if(players[i].wager>pending)
	pending=players[i].wager;
    }
  }
  factor2 = 0.0;
  if((double) factor1 / num_active >= 0.2) return FOLD;
  else if((double) factor1 / num_active < 0.0);

  int chips_left = SELF.pool-SELF.wager;
  double fraction_to_bet = 1.0 - (average_player_card-1.0)/((double)XRANGE-1.0);
  int to_bet = SELF.wager + (int) ((double)chips_left * fraction_to_bet);

  //make sure within bounds
  if(to_bet>SELF.pool)
    to_bet = SELF.pool;
  if(to_bet<=SELF.wager) {
    if(pending==SELF.wager)
      return CALL;
    else
      return FOLD;
  }

  if(pending>to_bet)
    return FOLD;
  else
    return WAGER(to_bet);        
}

void round_end(const struct player_data* players, unsigned int numplayers, unsigned int winnings)
{
	
}

void game_end()
{
	
}

