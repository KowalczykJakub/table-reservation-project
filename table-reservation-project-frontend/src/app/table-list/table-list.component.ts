import { Component, OnInit } from '@angular/core';
import {ReservationService} from "../reservation.service";
import {Table} from "../table";

@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {

  tables!: Table[];

  constructor(private reservationService: ReservationService) {
  }

  ngOnInit(): void {

    this.getTables();
  }

  private getTables() {
    this.reservationService.getTableList().subscribe(data => {
      this.tables = data;
    })
  }

}
