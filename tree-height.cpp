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
	size[j] = -1;   // stores number of children for each element
	height[j] = 1;  //intial height is 1 for all
      }
    for(int j =0; j< n; j++)

      {
	if(parent[j] == -1)
	  {
	    root = j;   //root element has doesn't have parent

	  }
	else
	  {
	    size[parent[j]] += 1;  // counting number of elements each node is parenting
	    child[parent[j]][size[parent[j]]] = j; // saving the list of children for each parent in a 2D array

	  }

      }
    int p = -1;
    // getting all lowest level elements

    for (int j = 0;j<n;j++)  {
      if (size[j] == -1){
	p++;
	lowest[p] = j;
      }
    }

    // trying to get the height .... checking if root has at least one child
    while(size[root] > -1){
      int k = -1;
      int temp[n];
      // will iterate through of elements of same level..starting from lowest level
      for (int j=0;j<=p;j++) {
	//if height of parent is less than child...height of parent become height of child + 1
	if(height[parent[lowest[j]]] <= (height[lowest[j]] )) {
	  height[parent[lowest[j]]] = height[lowest[j]] + 1;
	}
        size[parent[lowest[j]]] -= 1; 
        // When no more child left for the parent, it will be considered as child in next iteration
	if(size[parent[lowest[j]]] == -1){
	  k++;
	  temp[k] = parent[lowest[j]];
	}

      }    
      p = k;
      // parents from previous iteration were saved to be copied as new children to iterate over
      for (int c= 0; c<= k; c++){
	lowest[c] = temp[c];
      }    

    }   
    // height of the tree is same as height of the root starting from the bottom
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
