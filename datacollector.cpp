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
	int num_cow = atoi(argv[3]);
	string str;
	bool rs = false,es = false;
	
	while(cin>>str){
     	   if(str == "ROUND"){
		if(!rs) {
			rs = true;
			cout<<"ROUND_START"<<endl;
			es = false;
		}
	   }
	   if(str == "ENDROUND"){
		if(!es){
			es = true;
			rs = false;
			cout<<"ROUND_END"<<endl;
		}
	   }
	   if(str == "TURN"){
		tot++;
		int cow_num;
		for(int i = 1; i <= num_cow; i++){
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
		for(int i = 1; i <= num_cow; i++){
		   for(int j = 1; j <= 5; j++) cout<<turn_data[tot][i][j]<<" ";
		   cout<<endl;
		}
		cout<<endl;
	   }
	}
	return 0;
}
