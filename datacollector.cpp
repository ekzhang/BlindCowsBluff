#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
const int maxn = 100005;
int tot = 0,turn_cnt = 0;
int turn_data[1005][15][7];

int main(int argc,char*argv[]){
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	string str;
	while(cin>>str){
     	   if(str == "TURN"){
		tot++;
		int cow_num;
		for(int i = 1; i <= 6; i++){
			for(int j = 1; j <= 3; j++) cin>>str;
			cow_num = str[1] - '0';
			cin>>str;
			for(int j = 1; j <= 5; j++) cin>>turn_data[tot][i][j];
		}
		for(int j = 1; j <= 10; j++) {cin>>str;}
		int wage = 0;
		cout<<"Cow "<<cow_num<<endl;
		if(str == "WAGER") cin>>wage;
		cout<<"Action "<<str<<" "<<wage<<endl;
		for(int i = 1; i <= 5; i++){
		   for(int j = 1; j <= 5; j++) cout<<turn_data[tot][i][j]<<" ";
		   cout<<endl;
		}
		cout<<endl;
	   }
	}
	return 0;
}
