import { Component, OnInit } from '@angular/core';
import {Dish} from "../dish";
import {ReservationService} from "../reservation.service";

@Component({
  selector: 'app-dish-list',
  templateUrl: './dish-list.component.html',
  styleUrls: ['./dish-list.component.css']
})
export class DishListComponent implements OnInit {

  dishes!: Dish[];

  constructor(private reservationService: ReservationService) {
  }

  ngOnInit(): void {

    this.getDishes();
  }

  private getDishes() {
    this.reservationService.getDishList().subscribe(data => {
      this.dishes = data;
    })
  }

}
