#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<int, int>a, pair<int, int>b)
{
    if(a.second < b.second)
        return true;
    else if(a.second == b.second)
        return a.first < b.first;
    return false;
}


int main() 
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    int N; cin>>N;
    
    pair<int, int> *arr;
    arr = new pair<int, int>[N];
    
    for(int i = 0; i < N; i++)
    {
        cin >> arr[i].first >> arr[i].second;
    }

    sort(arr, arr + N, compare);    //compare값이 true이면 swap을 안 함.

    int cnt = 0;
    int lastTime;
    for(int i = 0; i < N; i++)
    {
        if(i == 0 || arr[i].first >= lastTime)
        {
            cnt++;
            lastTime = arr[i].second;
        }
    }

    cout << cnt;

    delete[] arr;
    return 0;
}