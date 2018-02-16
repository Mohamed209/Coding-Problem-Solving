#problem : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/psychic-powers/
# Solution:
#include <iostream>
#include <cstdlib>
#include <string>
#include <math.h>

using namespace std;

int main(int argc, char** argv) {
    string s;
    cin>>s;
    int i=0;
    int sum=0;
    int flag=0;
    while(s[i]!='\0')// loop all elements
    { 
        for(int j=i;j<=i+5;j++)// check every 6 consecutive numbers
        {
            sum+=s[j];
        }
        if(sum==288||sum==294)// if you found 6 consecutive ones or zeros (sum is ascii , because input is string)
        {
            flag=1;break;
        }
        i++;// move to next element
        sum=0;//reset sum
    }
    if(flag){cout<<"Sorry, sorry!"<<endl;}
    else if(flag==0){cout<<"Good luck!";}
    return 0;
}
