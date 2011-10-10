hand = imread('hand.ppm', 'ppm');
book = imread('book.ppm', 'ppm');
imagesc(hand);
figure;
imagesc(book);
data1 = normalize_and_label(hand,0);
data2 = normalize_and_label(book,1);
test_data = [data1; data2];
figure
hold on;
plot(data2(:,1), data2(:,2), '.');

plot(data1(:,1), data1(:,2), '.r');
plot(data1(:,1), data1(:,2), '.r');
