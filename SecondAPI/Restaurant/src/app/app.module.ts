import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { MenuComponent } from './menu/menu.component';
import { BookComponent } from './book/book.component';
import { ContactComponent } from './contact/contact.component';
import { SharedService } from './shared.service';
import{FormsModule, ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ViewBookingsComponent } from './view-bookings/view-bookings.component';

@NgModule({ 
  declarations: [
    AppComponent,
    HomeComponent,
    MenuComponent,
    BookComponent,
    ContactComponent,
    ViewBookingsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule 
  ],
  providers: [SharedService], 
  bootstrap: [AppComponent]
})
export class AppModule { }
