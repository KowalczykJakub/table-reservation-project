import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {HttpClientModule} from "@angular/common/http";
import { AddReservationComponent } from './add-reservation/add-reservation.component';
import {FormsModule} from "@angular/forms";
import {AppRoutingModule} from "./app-routing.module";
import { DishListComponent } from './dish-list/dish-list.component';
import { SendCancellationRequestComponent } from './send-cancellation-request/send-cancellation-request.component';
import { ConfirmCancellationRequestComponent } from './confirm-cancellation-request/confirm-cancellation-request.component';
import { FilterTablesComponent } from './filter-tables/filter-tables.component';
import { TableListComponent } from './table-list/table-list.component';

@NgModule({
  declarations: [
    AppComponent,
    AddReservationComponent,
    DishListComponent,
    SendCancellationRequestComponent,
    ConfirmCancellationRequestComponent,
    FilterTablesComponent,
    TableListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
