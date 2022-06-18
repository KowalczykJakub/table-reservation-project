import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilterTablesComponent } from './filter-tables.component';

describe('FilterTablesComponent', () => {
  let component: FilterTablesComponent;
  let fixture: ComponentFixture<FilterTablesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FilterTablesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FilterTablesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
