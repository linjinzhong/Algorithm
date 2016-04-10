/*
如何检测一个链表是否有环，如果有，那么如何确定环的起点
*/
int *head=list.GetHead();
if(head!=null){
	int *fastPtr=head;
	int *slowPtr=head;
	bool isCircular=true;
	do{
		if(fastPtr->next==null||fastPtr->Next->Next==null){
			isCircular=false;
			break;
		}	
		fastPtr=fastPtr->Next->Next;
		slowPtr=slowPtr->Next;
	}while(fastPtr!=slowPtr);
	//确定环的起点
	slowPtr=head;//慢指针移动到链表起点
	while(slowPtr!=fastPtr){//快慢指针同时向前移动一步，相遇时为环起点
		slowPtr=slowPtr->Next;
		fastPtr=fastPtr->Next;
	}
	cout<<"The starting point of the cycle is "<<slowPtr<<endl;
}
