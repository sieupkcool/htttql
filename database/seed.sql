INSERT INTO users (username, password, role) VALUES
('admin', 'admin_password', 'admin'),
('teacher1', 'teacher1_password', 'teacher'),
('student1', 'student1_password', 'student');

INSERT INTO departments (name) VALUES
('Computer Science'),
('Mathematics'),
('Physics');

INSERT INTO subjects (name, department_id) VALUES
('Data Structures', 1),
('Algorithms', 1),
('Calculus', 2),
('Linear Algebra', 2),
('Classical Mechanics', 3),
('Quantum Physics', 3);

INSERT INTO exams (name, subject_id, exam_date, duration) VALUES
('Midterm Exam - Data Structures', 1, '2023-10-15', 120),
('Final Exam - Algorithms', 1, '2023-12-20', 180),
('Midterm Exam - Calculus', 2, '2023-10-22', 90),
('Final Exam - Linear Algebra', 2, '2023-12-25', 120),
('Midterm Exam - Classical Mechanics', 3, '2023-10-29', 150),
('Final Exam - Quantum Physics', 3, '2023-12-30', 150);

INSERT INTO questions (exam_id, question_text, question_type, options, correct_answer) VALUES
(1, 'What is a linked list?', 'multiple_choice', '["A data structure", "A type of algorithm", "A programming language", "None of the above"]', 'A data structure'),
(1, 'What is the time complexity of binary search?', 'multiple_choice', '["O(n)", "O(log n)", "O(n log n)", "O(1)"]', 'O(log n'),
(2, 'Explain the concept of dynamic programming.', 'essay', NULL, NULL),
(3, 'What is the derivative of x^2?', 'multiple_choice', '["2x", "x^2", "x", "None of the above"]', '2x'),
(4, 'What is the eigenvalue of a matrix?', 'multiple_choice', '["A scalar", "A vector", "A matrix", "None of the above"]', 'A scalar'),
(5, 'Describe Newton\'s laws of motion.', 'essay', NULL, NULL),
(6, 'What is the uncertainty principle?', 'essay', NULL, NULL);