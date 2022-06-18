import { Component, OnInit } from '@angular/core';
import {ReservationService} from "../reservation.service";
import {Router} from "@angular/router";
import {TableFilterModel} from "../table-filter-model";
import {HttpErrorResponse} from "@angular/common/http";

@Component({
  selector: 'app-filter-tables',
  templateUrl: './filter-tables.component.html',
  styleUrls: ['./filter-tables.component.css']
})
export class FilterTablesComponent implements OnInit {

  tableFilterModel: TableFilterModel = new TableFilterModel()
  error: string = ""

  constructor(private reservationService: ReservationService,
              private router: Router) { }

  ngOnInit(): void {
  }

  confirmRequest() {
    this.reservationService.filterTables(this.tableFilterModel).subscribe(data => {
          console.log(data);
          this.goToTablesList();
        },
        (error: HttpErrorResponse) => {
          console.log(error)
          this.error = error.error.detail
        })
  }

  goToTablesList() {
    this.router.navigate(['/tables'])
  }

  onSubmit() {
    this.confirmRequest()
  }
}
