export class BookModel {
    constructor(
        public ReservationId: number,
        public ReservationDay:string,
        public ReservationHour:string,
        public Name:string,
        public PhoneNumber:string,
        public NumOfPersons:number
    ){}
}
