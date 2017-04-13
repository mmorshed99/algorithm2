#include <iostream>
#include <vector>
#include <algorithm>

class TreeHeight {
  int n;             
  std::vector<int> parent;

public:
  void read() {
    std::cin >> n;
    parent.resize(n);
    for (int i = 0; i < n; i++)
      std::cin >> parent[i];
  }

  int compute_height() {
    int maxHeight = 0;
    int root = -1;
    int child[100000][100000];
    int size[100000];
    int height[100000];
    int lowest[n];

    for(int j = 0; j<n; j++)
      {
	size[j] = -1;
	height[j] = 1;
      }
    for(int j =0; j< n; j++)

      {
	if(parent[j] == -1)
	  {
	    root = j;

	  }
	else
	  {
	    size[parent[j]] += 1;
	    child[parent[j]][size[parent[j]]] = j;

	  }

      }
    int p = -1;
    for (int j = 0;j<n;j++)  {
      if (size[j] == -1){
	p++;
	lowest[p] = j;
      }
    }

    while(size[root] > -1){
      int k = -1;
      int temp[n];
      for (int j=0;j<=p;j++) {
	if(height[parent[lowest[j]]] <= (height[lowest[j]] )) {
	  height[parent[lowest[j]]] = height[lowest[j]] + 1;
	}
        size[parent[lowest[j]]] -= 1; 
	if(size[parent[lowest[j]]] == -1){
	  k++;
	  temp[k] = parent[lowest[j]];
	}

      }    
      p = k;

      for (int c= 0; c<= k; c++){
	lowest[c] = temp[c];
      }    

    }   
    maxHeight = height[root];
    return maxHeight;
  }
};

int main() {
  std::ios_base::sync_with_stdio(0);
  TreeHeight tree;
  tree.read();
  std::cout << tree.compute_height() << std::endl;
}
