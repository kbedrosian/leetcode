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
    void printList(ListNode* head) {
        while (head != NULL) {
            cout << head->val;
            if (head->next != NULL) {
                cout << "->";
            }
            if (head->next != NULL && head->next->next == head) {
                cout << head->next->val << "...";
                break;
            }
            head = head->next;
        }
        cout << endl;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        // First count the nodes, so we can know when we're going to hit the end.
        int nodesLeft = 0;
        ListNode* currentNode = head;
        while (currentNode != NULL) {
            nodesLeft++;
            currentNode = currentNode->next;
        }

        ListNode* resultHead = NULL;

        // Maintain pointer to the node right before the next k-group.
        ListNode* prevKGroupNode = NULL;
        ListNode* currentKGroupNode = head;

        // Make sure there are at least k nodes left.
        while (nodesLeft >= k && k > 1) {
            // Reverse nodes until k have been reversed.
            int nodesReversed = 0;
            ListNode* currentRevNode = currentKGroupNode->next;
            ListNode* prevRevNode = currentKGroupNode;
            while (nodesReversed < k-1) {
                ListNode* nextRevNode = currentRevNode->next;
                currentRevNode->next = prevRevNode;
                prevRevNode = currentRevNode;
                currentRevNode = nextRevNode;
                nodesReversed++;
            }
            nodesLeft -= k;
            // Connect the end of the reversed k-group (currentKGroupNode) to
            // currentRevNode, which is the next node after the k-group in the
            // original list.
            currentKGroupNode->next = currentRevNode;

            // If prevKGroupNode is set, it is the node previous to the k-group in
            // the original list, so connect that to the beginning of the reversed
            // k-group.
            // If it is not set, then it means we're at the head of the list, so set
            // resultHead.
            if (prevKGroupNode != NULL) {
                prevKGroupNode->next = prevRevNode;
            } else {
                resultHead = prevRevNode;
            }

            // Now update prevKGroupNode and currentKGroupNode.
            prevKGroupNode = currentKGroupNode;
            currentKGroupNode = currentRevNode;
        }
        if (resultHead == NULL) {
            return head;
        } else {
            return resultHead;
        }
    }
};
