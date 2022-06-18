import { Component, OnInit } from '@angular/core';
import {ReservationService} from "../reservation.service";
import {Router} from "@angular/router";
import {CancellationRequest} from "../cancellation-request";
import {HttpErrorResponse} from "@angular/common/http";

@Component({
  selector: 'app-send-cancellation-request',
  templateUrl: './send-cancellation-request.component.html',
  styleUrls: ['./send-cancellation-request.component.css']
})
export class SendCancellationRequestComponent implements OnInit {

  cancellationCode: CancellationRequest = new CancellationRequest();
  error: string = ""

  constructor(private reservationService: ReservationService,
              private router: Router) { }

  ngOnInit(): void {
  }

  sendRequest() {
    this.reservationService.cancellationOfReservationRequest(this.cancellationCode.id).subscribe(data => {
          console.log(data);
          this.goToHomePage();
        },
        (error: HttpErrorResponse) => {
          console.log(error)
          this.error = error.error.detail
        })
  }

  goToHomePage() {
    this.router.navigate(['/confirm-cancellation-request'])
  }

  onSubmit() {
    this.sendRequest()
  }
}
