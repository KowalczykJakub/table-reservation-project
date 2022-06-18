import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from "@angular/router";
import {AddReservationComponent} from "./add-reservation/add-reservation.component";
import {DishListComponent} from "./dish-list/dish-list.component";
import {SendCancellationRequestComponent} from "./send-cancellation-request/send-cancellation-request.component";
import {ConfirmCancellationRequestComponent} from "./confirm-cancellation-request/confirm-cancellation-request.component";
import {TableListComponent} from "./table-list/table-list.component";
import {FilterTablesComponent} from "./filter-tables/filter-tables.component";


const routes: Routes = [
  {path: 'add-reservation', component: AddReservationComponent},
  {path: '', component: DishListComponent},
  {path: 'filter-tables', component: FilterTablesComponent},
  {path: 'tables', component: TableListComponent},
  {path: 'send-cancellation-request', component: SendCancellationRequestComponent},
  {path: 'confirm-cancellation-request', component: ConfirmCancellationRequestComponent}
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
