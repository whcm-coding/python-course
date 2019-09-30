#include <stdio.h>

int main()
{
  int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int i, j;
  //奇数
  int oddNumbers[10] = {};
  //偶数
  int evenNumbers[10] = {};
  int oddIdx = 0;
  int evenIdx = 0;
  for (i = 0; i < 10; i++)
  {
    if (arr[i] % 2 == 0)
    {
      evenNumbers[evenIdx++] = arr[i];
    }
    else
    {
      oddNumbers[oddIdx++] = arr[i];
    }
  }
  printf("奇数");
  for (i = 0; i < oddIdx; i++)
  {
    printf("%d", oddNumbers[i]);
  }
  printf("偶数");
  for (j = 0; j < evenIdx; j++)
  {
    printf("%d", evenNumbers[j]);
  }
  return 0;
}