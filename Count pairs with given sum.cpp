#problem:http://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum/0
#solution:
#include <iostream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        int N,K;
        int counter=0;
        cin>>N>>K;
        int array[N];
        for(int j=0;j<N;j++)
        {
            cin>>array[j];
        }
        for(int m=0;m<N-1;m++)
        {
            for(int l=m+1;l<N;l++)
            {
                if(array[m]+array[l]==K)
                {
                    counter++;
                }
            }
        }
        cout<<counter<<endl;
    }
    return 0;
}
