function g = discriminant( data, mu, sigma, p )

    g = zeros(size(data,1), 2);
    
    for i = 1:2
        for j = 1:size(data,1)
            g(j,i) = log(p(i));
            for n = 1:2
                g(j,i) = g(j,i) - log(sigma(i,n)) - ((data(j,n) - mu(i,n))^2)/(2*sigma(i,n)^2);
            end
        end
    end

end

