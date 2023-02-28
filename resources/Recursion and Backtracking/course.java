import java.util.*;
import java.math.*;
import java.text.*;
import java.io.*;
 
public class Main{
	//Recursion Problems Solution:
	
	public static int Sum(int x){
		if(x == 1)return 1;
		return x + Sum(x - 1);
	}
	
	public static boolean isSymmetric(int left, int right, int[] arr){
			if(left >= right)return true;
			if(arr[left] != arr[right])return false;
			
			return isSymmetric(left + 1, right - 1, arr);
	}
	
	public static int factorial(int n){
		if(n <= 1) return 1;
		return n * factorial(n-1);
	}
	
	public static void threeNplusOne(int n){
		System.out.print(n + " ");
		if(n == 1) return;
		if(n % 2 == 1) 
				threeNplusOne(3*n + 1);
		else
				threeNplusOne(n/2);
	}
	
	//Flood-Fill Code:
	
	public static void FloodFill(int x, int y, int m, int n, int[][] grid){
		if(x < 0 || y < 0 || x >= n || y >= m || grid[y][x] == 0)
			return;
		
		grid[y][x] = 0;
		
		FloodFill(x - 1, y, m, n, grid);
		FloodFill(x, y - 1, m, n, grid);
		FloodFill(x, y + 1, m, n, grid);
		FloodFill(x + 1, y, m, n, grid);
		
	}
 
	//Binary-Search Code:
	public static int binarySearch(int left, int right, int[] Array, int value){
		
		if(left > right)return -1;
		
		int mid = left + (right - left)/2;
		
		if(Array[mid] == value)return mid;
		
		if(Array[mid] < value)
			return binarySearch(mid + 1, right, Array, value);
		else
			return binarySearch(left, mid - 1, Array, value);
	}
	
	//Fibonacci Series- naive:
	public static int fibonacci(int n){
		if(n <= 1) return n;
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
	
	
	//Fibonacci Series-memoization
	public static int fibonacci(int n, int[] Memo){
		if(n <= 1)return n;
		
		if(Memo[n] != -1)return Memo[n];
 
		return Memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
	}
	
	//Tribonacci Naive
	public static int Tribonacci(int n){
		if(n <= 2)return n;
		
		return Tribonacci(n - 1) - Math.max(Tribonacci(n-2), Tribonacci(n-3));
	}
	
	//Merge-Sort
	public static void MergeSort(int left, int right, int[] Array){
		if(left >= right)return;
		
		int mid = left + (right - left)/2;
		
		MergeSort(left, mid, Array);
		MergeSort(mid + 1, right, Array);
		Merge(left, mid, right, Array);
	}
	
	static void Merge(int left, int mid, int right, int[] Array){
		int ln = mid - left;
		int rn = right - mid + 1;
		
		int[] LArr = new int[ln];
		int[] RArr = new int[rn];
		
		for(int i = 0; i < ln; i++)
			LArr[i] = Array[i + left];
		
		for(int i = 0; i < rn; i++)
			RArr[i] = Array[i + mid + 1];
		
		int i = 0, j = 0, k = left;
		
		while(i < ln && j < rn){
			if(LArr[i] <= RArr[j]){
				Array[k] = LArr[i];
				i++;
			}else{
				Array[k] = RArr[j];
				j++;
			}
			
			k++;
		}
		
		while(i < ln){
			Array[k] = LArr[i];
			k++; i++;
		}
		
		while(j < rn){
			Array[k] = RArr[j];
			k++; j++;
		}
	}
	
	//Binary Strings
	public static void BString(int i, int n, int Array[]){
		if(i == n){
			for(int l: Array)
					System.out.print(l + " ");
			System.out.println();
			return;
		}
		Array[i] = 0;
		BString(i + 1, n, Array);
		//Backtracking
		
		Array[i] = 1;
		BString(i + 1, n, Array);
		
	}
	
	//k-Ary Strings
	public static void kAry(int i, int n, int k, int Array[], int Basket[]){
			if(i == n){
				for(int l: Array)
					System.out.print(l + " ");
				System.out.println();
			return;
		}
		
		for(int l = 0; l < k; l++){
			Array[i] = Basket[l];
			kAry(i + 1, n, k, Array, Basket);
		}
	}
	
	//Magnet-Chain Naive:
	public static int Chain(int i, int j, int gSize){
		if(j < 0|| j>= gSize)return 0;
		
		if(i == gSize)return 1;
		
		i++;
		
		return Chain(i, j - 1, gSize) +
			   Chain(i, j, gSize) +
			   Chain(i, j + 1, gSize);
	}
	
	//Magnet-Chain Memoization:
	public static int Chain(int i, int j, int gSize, int[][]Memo){
		if(j < 0|| j>= gSize)return 0;
		
		if(i == gSize)return 1;
		
		// -1 signifies "Unvisited"
		if(Memo[i][j] != -1)return Memo[i][j];
		
		i++;
		
		return Memo[i][j] = Chain(i, j - 1, gSize) +
							Chain(i, j, gSize) +
							Chain(i, j + 1, gSize);
	}
	
	//Maze-Problem Simplified
	
	//Naive
	public static int MazeRat(int i, int j, int m, int n, int[][]Maze){
		if(i < 0 || j < 0 || i == m || j == n)return 0;
		
		if(Maze[i][j] == -1)return 0;
		
		if(i == m - 1 && j == n - 1)return 1;
		
		return MazeRat(i + 1, j, m, n, Maze) +
			   MazeRat(i, j + 1, m, n, Maze);
	}
	
	//Memoization
	public static int MazeRat(int i, int j, int m, int n, int[][]Maze, int[][]Memo){
		if(i < 0 || j < 0 || i == m || j == n)return 0;
		
		if(Maze[i][j] == -1)return 0;
		
		if(i == m - 1 && j == n - 1)return 1;
		
		if(Maze[i][j] != -1)return Memo[i][j];
		
		return Memo[i][j] = MazeRat(i + 1, j, m, n, Maze) +
							MazeRat(i, j + 1, m, n, Maze);
	}
	
	
	//Gold Collector
	
	//Memoization
	public static int Collect(int i, int n, int Array[], int Memo[]){
		if(i >= n)return 0;
		if(Memo[i] != -1) return Memo[i];
		
		return Memo[i] = Math.max(Collect(i + 1, n, Array, Memo),
								  Collect(i + 2, n, Array, Memo) + Array[i]);
	}
		
	//Tabulation
	public static int Collect(int n, int Array){
		int Table[] = new int[n];
		
		Table[0] = Array[0];
		Table[1] = Math.max(Array[1], Table[0]);
		
		for(int i = 2; i < n; i++)
			Table[i] = Math.max(Table[i - 1], Table[i -2] + Array[i]);
		
		return Table[n - 1];
	}
	
	//Permutations
	
	//Naive
	public static void Arrange(int i, int n, int[] Array, int[] Basket){
		if(i == n){
			int temp[] = new int[n];
			for(int l = 0; l < n; l++)
				temp[i] = Array[i];
			
			Arrays.sort(temp);
			
			boolean key = true;
			
			for(int l = 1; l < n; l++){
				if(temp[l] == temp[l - 1]){
					key = false;
					break;
				}
			}
			
			if(key){
				for(int l = 0; l < n; l++)
					System.out.print(Array[i] + " ");
				System.out.println();
			}
			
			return;
		}
		
		for(int l = 0; l < n; l++){
			Array[i] = Basket[l];
			Arrange(i + 1, n, Array, Basket);
		}
		
	}
	
	//Optimized
	public static void Arrange(int i, int n, int[]Array, int[]Basket){
		if(i == n){
			for(int l = 0; l < n; l++)
				System.out.print(Array[l] + " ");
			System.out.println();
			
			return;
		}
		
		for(int l = 0; l < n; l++){
			if(Basket[l] == -1)continue;
			Array[i] = Basket[l];
			Basket[l] = -1;
			Arrange(i + 1, n, Array, Basket);
			Basket[l] = Array[i];
		}
	}
	
	//More optimized
	static void swap(int i, int j, int[] arr){
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	
	public static void Arrange(int i, int n,  int[]Basket){
		if(i == n){
			for(int l = 0; l < n; l++)
				System.out.print(Basket[l] + " ");
			System.out.println();
			
			return;
		}
		
		for(int l = i; l < n; l++){
			swap(l, i, Basket);
			Arrange(i + 1, n, Basket);
			swap(l, i, Basket);
		}
	}
	
	//Maze Problem Revised
	public static int MazeRat(int i, int j, int m, int n, int Maze[]){
		if(i < 0 || j < 0 || i == m || j == n)return 0;
		
		if(Maze[i][j] < 0)return 0;
		
		if(Maze[i][j] == 2) return 1;
		
		Maze[i][j] -= 5;
		
		int k = 0;
		k += MazeRat(i - 1, j, m, n, Maze);
		k += MazeRat(i, j - 1, m, n, Maze);
		k += MazeRat(i + 1, j, m, n, Maze);
		k += MazeRat(i, j + 1, m, n, Maze);
 
		Maze[i][j] += 5;
		return k;
	}
	
	//Knight Problem
	public static int Knight(int i, int j, int m, int n, int Board[], int Moves[][]){
		if(i < 0 || j < 0 || i >= m || j >= n)return 0;
		
		if(Board[i][j] < 0)return 0;
		
		if(Board[i][j] == 2) return 1;
		
		Board[i][j] -= 5;
		
		int k = 0;
		for(int l = 0; l < 8; l++){
			int x = Moves[l][0];
			int y = Moves[l][1];
			
			k += Knight(i + y, j + x, m, n, Board, Moves);
		}
		
		Board[i][j] += 5;
		
		return k;
	}
	
	//N-queen Problem
	static void swap(int i, int j, int[] arr){
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	
	public static void Arrange(int i, int n,  int[]Basket){
		if(i == n){
			if(isValid(Basket, n)){
				print(Basket, n);
			}
			
			return;
		}
		
		for(int l = i; l < n; l++){
			swap(l, i, Basket);
			Arrange(i + 1, n, Basket);
			swap(l, i, Basket);
		}
	}
	
	static boolean isValid(int[] Basket, int n){
		
		for(int i = 0; i < n; i++)
			for(int j = i + 1; j < n; j++)
				if(Math.abs(i - j) == Math.abs(Basket[i] - Basket[j]))
					return false;
		
		return true;
	}
	
	static void print(int[] Basket, int n){
		int Board[][] = new int[n][n];
		
		for(int[] i: Board)
			Arrays.fill(i, 0);
		
		for(int l = 0; l < n; l++)
			Board[l][Basket[l]] = 1;
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				System.out.print(Board[i][j] + " ");
			}
			
			System.out.println();
		}
	}
	
	
}