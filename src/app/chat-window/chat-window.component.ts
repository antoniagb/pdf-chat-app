// chat-window.component.ts
import { Component } from '@angular/core';
import { Message } from '../model/message.model';
@Component({
  selector: 'app-chat-window',
  templateUrl: './chat-window.component.html',
  styleUrls: ['./chat-window.component.scss']
})
export class ChatWindowComponent {
  messages: Message[] = []; // Use Message interface here
  newMessage: string = '';

  sendMessage() {
    if (this.newMessage.trim()) {
      const newMessage: Message = { text: this.newMessage }; // Create a new Message object
      this.messages.push(newMessage);
      this.newMessage = '';

      // Call ChatGPT API here to generate bot response
    }
  }
}



/* chat-window.component.ts
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-chat-window',
  templateUrl: './chat-window.component.html',
  styleUrls: ['./chat-window.component.scss']
})
export class ChatWindowComponent {
  messages: string[] = [];
  userInput: string = '';

  constructor(private http: HttpClient) {}

  sendMessage() {
    if (this.userInput.trim() === '') return;

    this.messages.push(`User: ${this.userInput}`);
    this.http.post<any>('YOUR_CHATGPT_BACKEND_URL', { message: this.userInput })
      .subscribe(response => {
        this.messages.push(`ChatGPT: ${response.message}`);
      });

    this.userInput = '';
  }}*/
