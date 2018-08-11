//problem :
//https://www.hackerrank.com/challenges/balanced-brackets/problem
//Solution
#include <iostream.h>
#include <string.h>
using namespace std;
// Complete the isBalanced function below.
string isBalanced(string s) {
    stack <char> st;
    char x;
    if (s[0]==')'||s[0]=='}'||s[0]==']')
    {
        return "NO";
    }
    else
    {
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='('||s[i]=='{'||s[i]=='[')
            {
                st.push(s[i]);
                continue;
            }
            switch(s[i])
            {
                case ')':
                    x=st.top();
                    st.pop();
                    if (x=='{' || x=='['){return "NO";}
                    break;  
                case '}':
                    x=st.top();
                    st.pop();
                    if(x=='('||x=='['){return "NO";}
                    break;
                case ']':
                    x=st.top();
                    st.pop();
                    if(x=='('||x=='{'){return "NO";}
                    break;
            }
        }
        if(st.empty()){return "YES";}
        else {return "NO";}
    }
}
