import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {Reservation} from "../reservation";
import {ReservationService} from "../reservation.service";
import {HttpErrorResponse} from "@angular/common/http";

@Component({
  selector: 'app-add-reservation',
  templateUrl: './add-reservation.component.html',
  styleUrls: ['./add-reservation.component.css']
})
export class AddReservationComponent implements OnInit {

  reservation: Reservation = new Reservation();
  error: string = ""

  constructor(private reservationService: ReservationService,
              private router: Router) { }

  ngOnInit(): void {
  }

  saveReservation() {
    this.reservationService.createReservation(this.reservation).subscribe(data => {
          console.log(data);
          this.goToHomePage();
        },
        (error: HttpErrorResponse) => {
          console.log(error)
          this.error = error.error.detail
        })
  }

  goToHomePage() {
    this.router.navigate(['/'])
  }

  onSubmit() {
    this.saveReservation()
  }
}
