def weight_on_planets():
      # write your code here
      #get weight on earth
      earth_weight_string = input('What do you weigh on earth? ')
      print('')

      #change weight to an int
      earth_weight = int(earth_weight_string)

      #calc weight on other planets
      mars_weight = 0.38 * earth_weight
      jupiter_weight = 2.34 * earth_weight

      #print output
      print("On Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds." .format(mars_weight, jupiter_weight))

if __name__ == '__main__':
      weight_on_planets()