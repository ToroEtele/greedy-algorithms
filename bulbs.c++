#include <iostream>

using namespace std;

int bulbs(bool A[], int length)
{
  int cost = 0;

  for (int i = 0; i < length; i++)
  {
    if (cost % 2 == 1)
      A[i] = !A[i];

    if (A[i] == false)
      cost++;
  }

  return cost;
}

int main()
{
  cout << "Hello world!" << endl;
  return 0;
}
