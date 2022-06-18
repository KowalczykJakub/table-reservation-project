import { Component, OnInit } from '@angular/core';
import {ReservationService} from "../reservation.service";
import {Router} from "@angular/router";
import {CancellationCode} from "../cancellation-code";
import {CancellationRequest} from "../cancellation-request";
import {HttpErrorResponse} from "@angular/common/http";

@Component({
  selector: 'app-confirm-cancellation-request',
  templateUrl: './confirm-cancellation-request.component.html',
  styleUrls: ['./confirm-cancellation-request.component.css']
})
export class ConfirmCancellationRequestComponent implements OnInit {

  cancellationCode: CancellationCode = new CancellationCode();
  cancellationRequest: CancellationRequest = new CancellationRequest()
  error: string = ""

  constructor(private reservationService: ReservationService,
              private router: Router) { }

  ngOnInit(): void {
  }

  confirmRequest() {
    this.reservationService.deleteReservation(this.cancellationRequest.id, this.cancellationCode.verificationCode).subscribe(data => {
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
    this.confirmRequest()
  }

}
