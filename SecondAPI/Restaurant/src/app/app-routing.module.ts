import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BookComponent } from './book/book.component';
import { ContactComponent } from './contact/contact.component';
import { HomeComponent } from './home/home.component';
import { MenuComponent } from './menu/menu.component';
import { ViewBookingsComponent } from './view-bookings/view-bookings.component';

const routes: Routes = [
  {path:'Home',component:HomeComponent},
  {path:'Menu',component:MenuComponent},
  {path:'Book',component:BookComponent},
  {path:'Contact',component:ContactComponent},
  {path:'ViewBookings',component:ViewBookingsComponent}
   
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
