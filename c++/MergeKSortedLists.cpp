/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* resultHead = NULL;
        ListNode* resultCurrent = NULL;
        // Remove empty lists.
        lists.erase(
            remove_if(lists.begin(), lists.end(),
                      [](ListNode* l) { return l == NULL; }),
            lists.end());
        while (!lists.empty()) {
            // Find minimum node.
            vector<ListNode*>::iterator minIter;
            int min = INT_MAX;
            for (auto it = lists.begin(); it != lists.end(); it++) {
                if ((*it)->val < min) {
                    min = (*it)->val;
                    minIter = it;
                }
            }
            
            // Remove the min node from its respective list.
            ListNode* minNode = *minIter;
            if (minNode->next == NULL) {
                lists.erase(minIter);
            } else {
                *minIter = minNode->next;
                minNode->next = NULL;
            }
            
            // Add the min mode to the result list.
            if (resultHead == NULL) {
                resultHead = resultCurrent = minNode;
            } else {
                resultCurrent->next = minNode;
                resultCurrent = minNode;
            }
        }
        return resultHead;
    }
};
