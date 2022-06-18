import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SendCancellationRequestComponent } from './send-cancellation-request.component';

describe('SendCancellationRequestComponent', () => {
  let component: SendCancellationRequestComponent;
  let fixture: ComponentFixture<SendCancellationRequestComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SendCancellationRequestComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SendCancellationRequestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
