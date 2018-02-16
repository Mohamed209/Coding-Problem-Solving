# Problem : https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/maximum-and/
# Solution :
#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {
    int T;
    long int A,B;
    long int max=0;
    cin>>T;
    for(int i=0;i<T;i++)//input test cases
    {
        cin>>A>>B;//input A,B
        for(int j=A;j<B;j++)// loop all pairs between A,B
        {
            for(int k=j+1;k<=B;k++)
            {
                if((k&j)>max){max=(k&j);}
            }
        }
        cout<<max<<endl;
        max=0;//reset max for next test case
    }
    return 0;
}
