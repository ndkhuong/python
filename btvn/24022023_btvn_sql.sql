-- Create table
CREATE TABLE haisan (
	ma int NULL,
	ten ntext NULL,
	gia int NULL,
	diachi char(50) NOT NULL
);

-- Insert 10 rows
INSERT INTO haisan (ma, ten, gia, diachi) VALUES
('1', N'Nghêu', '10000', 'HCM'),
('2', N'Sò', '20000', 'HN'),
('3', N'Ốc', '30000', 'HCM'),
('4', N'Hến', '40000', 'HCM'),
('5', N'Tôm', '50000', 'HCM'),
('6', N'Cua', '60000', 'HCM'),
('7', N'Ghẹ', '70000', 'HCM'),
('8', N'Cá bóp', '80000', 'HCM'),
('9', N'Cá da bò', '90000', 'HCM'),
('10', N'Cá đuối', '100000', 'HN');

-- Find gia > 10000
SELECT * FROM haisan WHERE gia > 10000;

-- Set gia = 8000 where gia > 10000
UPDATE haisan SET gia = 8000 WHERE gia > 10000;
