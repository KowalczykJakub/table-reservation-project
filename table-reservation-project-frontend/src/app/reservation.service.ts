import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Reservation} from "./reservation";
import {Observable} from "rxjs";
import {Dish} from "./dish";
import {Table} from "./table";
import {TableFilterModel} from "./table-filter-model";

@Injectable({
  providedIn: 'root'
})
export class ReservationService {

  private baseUrl = "http://localhost:8000/reservations";

  constructor(private httpClient: HttpClient) { }

  getReservationList(): Observable<Reservation[]> {
    return this.httpClient.get<Reservation[]>(`${this.baseUrl}`);
  }

  getTableList(): Observable<Table[]> {
    return this.httpClient.get<Table[]>(`http://localhost:8000/tables`);
  }

  filterTables(tableFilterModel: TableFilterModel): Observable<Object> {
    return this.httpClient.post(`http://localhost:8000/tables`, tableFilterModel);
  }

  getDishList(): Observable<Dish[]> {
    return this.httpClient.get<Dish[]>(`http://localhost:8000/dishes`);
  }

  createReservation(reservation: Reservation): Observable<Object> {
    return this.httpClient.post(`${this.baseUrl}`, reservation);
  }

  cancellationOfReservationRequest(id: String): Observable<Object>{
    return this.httpClient.put(`${this.baseUrl}/${id}`, id);
  }

  deleteReservation(id: String, code: String): Observable<Object>{
    return this.httpClient.delete(`${this.baseUrl}/${id}/${code}`);
  }
}
