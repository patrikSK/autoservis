CREATE TABLE Car (
  id int(11) NOT NULL,
  date date NOT NULL,
  type text NOT NULL,
  brand text NOT NULL,
  model text NOT NULL,
  problem text NOT NULL,
  owner_id int(11) NOT NULL

  PRIMARY KEY (id),
  FOREIGN KEY (owner_id) REFERENCES Owner(id)
  ON DELETE CASCADE 
  ON UPDATE CASCADE
) ;
