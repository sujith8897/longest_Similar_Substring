
def longestSimilarSubstring(arr1,arr2):
	n=len(arr1)
	m=len(arr2)

	dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
	maxx=0

	for i in range(1,n+1):
		for j in range(1,m+1):

			if arr1[i-1] == arr2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
				if(maxx < dp[i][j]):
					maxx = dp[i][j]
					x = i-1
					y = j-1

	result=[]
	for i in range(maxx):
		result.append(arr1[x-i])
	result = result[::-1]
	return result


if __name__=="__main__":

	print('Enter array 1')
	arr1 = list(map(int,input().split()))
	
	print('Enter array 2')
	arr2 = list(map(int,input().split()))


	result = longestSimilarSubstring(arr1,arr2)

	n = len(result)

	print('(',end="")
	for i in range(n):
		if i < n-1:
			print(result[i],end=",")
		else:
			print(result[i],end=")")

