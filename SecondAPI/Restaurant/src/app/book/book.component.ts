import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service'; 
import { BookModel } from '../book-model';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit {

  
  bookModel = new BookModel(1,"day-select","hour-select","koushik","9087654321",4);

  constructor(private service:SharedService) { }

  ngOnInit(): void {
  }

  bookTable()
  {
    var val = {
      "ReservationId" : "",
      "ReservationDay" : this.bookModel.ReservationDay,
      "ReservationHour" : this.bookModel.ReservationHour,
      "Name": this.bookModel.Name,
      "Phonenumber" : this.bookModel.PhoneNumber,
      "Numberofpersons": this.bookModel.NumOfPersons
  };
    this.service.bookTable(val).subscribe(res=>{
      alert(res.toString()
        + "\nSENT DATA:\nReservationId:" + "" +
        " ReservationDay:" + this.bookModel.ReservationDay+
        " ReservationHour:" + this.bookModel.ReservationHour+
        " Name:" + this.bookModel.Name +
        " Phonenumber:" + this.bookModel.PhoneNumber +
        " Numberofpersons:" + this.bookModel.NumOfPersons
      );
    });
  }

}
