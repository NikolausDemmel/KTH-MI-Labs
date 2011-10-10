function rg_im = normalize_and_label(im, label)

im = double(im);
rg_im = [];
for y=1:size(im,1)
     for x=1:size(im,2)
        s = sum(im(y,x,:));
        if (s > 0)
            rg_im = [rg_im; im(y,x,1)/s im(y,x,2)/s label];
        end
     end
end