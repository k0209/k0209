import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service'; 

@Component({
  selector: 'app-view-bookings',
  templateUrl: './view-bookings.component.html',
  styleUrls: ['./view-bookings.component.css']
})
export class ViewBookingsComponent implements OnInit {

  ReservationList:any=[];
  constructor(private service:SharedService) { } 

  refreshReservationList()
  {
    this.service.getReservationList().subscribe(data=>{
    this.ReservationList=data;});
  }

  ngOnInit(): void {
    this.refreshReservationList();
  }
  deleteClick(item:any)
  {
  if(confirm("Are you sure ??"))
  {
    this.service.deletereservation(item.reservation).subscribe(data=>{
      alert(data.toString());
      this.refreshReservationList();
    });
  } 
} 
} 
