import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service'; 

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit {

  ReservationId:number= 1;
  ReservationDay:string="day-select";
  ReservationHour:string="hour-select";
  Name:string="";
  PhoneNumber:string="";
  NumOfPersons:number=1;

  constructor(private service:SharedService) { }

  ngOnInit(): void {
  }

  bookTable()
  {
    var val = {
      "ReservationId" : "",
      "ReservationDay" : this.ReservationDay,
      "ReservationHour" : this.ReservationHour,
      "Name": this.Name,
      "Phonenumber" : this.PhoneNumber,
      "Numberofpersons": this.NumOfPersons
    };
    this.service.bookTable(val).subscribe(res=>{
      alert(res.toString()
        // + "\nSENT DATA:\nReservationId:" + "" +
        // " ReservationDay:" + this.ReservationDay+
        // " ReservationHour:" + this.ReservationHour+
        // " Name:" + this.Name +
        // " Phonenumber:" + this.PhoneNumber +
        // " Numberofpersons:" + this.NumOfPersons
      );
    });
  }

}
