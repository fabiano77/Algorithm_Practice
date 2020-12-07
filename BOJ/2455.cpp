#include <iostream>
using namespace std;

int main(void)
{
    int max(0);
    int count(0);
    int in, out;
    for (int i = 0; i < 4; i++)
    {
        cin >> out >> in;
        count -= out;
        count += in;
        if(count > max) max = count;
    }
    cout << max;

    return 0;
}
