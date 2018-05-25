#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
const int maxn = 100005;
struct data{
	string da[10];
	string action[10];
} D[maxn];
int tot = 0;
int main(int arg,char *argv[]){
	freopen(argv[0],"r",stdin);
	string str;
	while(cin>>str){
		if(str.find("TURN") != string::npos && str.find("[5]") != string::npos){
			string tmp;
			tot++;
			for(int i = 1; i <= 6; i++){
				cin>>D[tot].da[i];
			}
		}
		
