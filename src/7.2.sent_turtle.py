from typing import Dict, List, Optional

class PostOffice:
    def __init__(self, usernames: List[str]):
        self.message_id = 0
        self.boxes: Dict[str, List[dict]] = {user: [] for user in usernames}
        
    def send_message(self, sender: str, recipient: str, title: str, body: str, urgent: bool = False) -> int:
        """Send a message to a recipient's mailbox.
        
        Args:
            sender: Name of the sender
            recipient: Name of the recipient
            title: Message title
            body: Message content
            urgent: If True, message goes to top of inbox
            
        Returns:
            The message ID
            
        Raises:
            KeyError: If recipient doesn't exist
        """
        if recipient not in self.boxes:
            raise KeyError(f"Recipient '{recipient}' does not exist")  # Changed to KeyError
            
        self.message_id += 1
        message = {
            'id': self.message_id,
            'title': title,
            'body': body,
            'sender': sender,
            'unread': True
        }
        
        if urgent:
            self.boxes[recipient].insert(0, message)
        else:
            self.boxes[recipient].append(message)
            
        return self.message_id

    def read_inbox(self, username: str, N: Optional[int] = None) -> List[dict]:
        """Read messages from a user's inbox."""
        mailbox = self.boxes.get(username, [])
        messages = mailbox[:N] if N is not None else mailbox.copy()
        
        for msg in messages:
            msg['unread'] = False
            
        return messages

    def search_inbox(self, username: str, search_string: str) -> List[dict]:
        """Search a user's inbox for messages containing search string."""
        if username not in self.boxes:
            return []
            
        search_lower = search_string.lower()
        return [
            msg for msg in self.boxes[username]
            if (search_lower in msg.get('title', '').lower() or 
                search_lower in msg.get('body', '').lower() or
                search_lower in msg.get('sender', '').lower())
        ]