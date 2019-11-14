INSERT INTO Table4 
SELECT 	t3.InternalNumber,
		concat(t1.Name, ' ', t2.Surname) as 'Name/Surname',
		t3.Position,
		t1.Salary / 12 as 'Salary/Month',
		t2.Taxes,
		t2.Month
FROM Table1 t1
INNER JOIN Table2 t2
	ON t1.ID = t2.EmployeeID
INNER JOIN Table3 t3
	on t1.ID = t3.EmployeeID

SELECT * FROM Table4