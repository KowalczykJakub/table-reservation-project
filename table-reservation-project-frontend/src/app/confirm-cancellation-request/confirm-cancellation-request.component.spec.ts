import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfirmCancellationRequestComponent } from './confirm-cancellation-request.component';

describe('ConfirmCancellationRequestComponent', () => {
  let component: ConfirmCancellationRequestComponent;
  let fixture: ComponentFixture<ConfirmCancellationRequestComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConfirmCancellationRequestComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfirmCancellationRequestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
